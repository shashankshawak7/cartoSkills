BLOCK-LEVEL ON ERROR UNDO, THROW.

CLASS legacy.order_manager INHERITS legacy.base_manager:

    /* 1. Temp-Table (Global Data Structure) */
    DEFINE TEMP-TABLE ttOrder NO-UNDO
        FIELD OrderID AS INTEGER
        FIELD CustID  AS INTEGER
        FIELD Total   AS DECIMAL
        INDEX idxID IS PRIMARY UNIQUE OrderID.

    /* 2. Constructor & Closure-like Logic */
    CONSTRUCTOR PUBLIC order_manager():
        EMPTY TEMP-TABLE ttOrder.
    END CONSTRUCTOR.

    /* 3. OOABL Method with Inheritance and Parameter Mapping */
    METHOD OVERRIDE PUBLIC VOID Process(INPUT piOrderID AS INTEGER):
        DEFINE VARIABLE iCount AS INTEGER NO-UNDO.
        
        SUPER:Process(piOrderID). /* Base class call */
        
        RUN CalculateTotal(INPUT piOrderID, OUTPUT iCount).
        
        IF iCount > 0 THEN
            MESSAGE "Order Processed" VIEW-AS ALERT-BOX.
    END METHOD.

    /* 4. Internal Procedure (Legacy Procedural Logic) */
    PROCEDURE CalculateTotal:
        DEFINE INPUT  PARAMETER piOrderID AS INTEGER NO-UNDO.
        DEFINE OUTPUT PARAMETER poCount    AS INTEGER NO-UNDO.
        
        FIND FIRST ttOrder WHERE ttOrder.OrderID = piOrderID NO-LOCK NO-ERROR.
        
        IF AVAILABLE ttOrder THEN
            poCount = 1.
        ELSE
            poCount = 0.
    END PROCEDURE.

    /* 5. Trigger (Event-based Logic) */
    ON 'VALUE-CHANGED' OF ttOrder.OrderID ANYWHERE DO:
        MESSAGE "Order ID changed manually" VIEW-AS ALERT-BOX.
    END.

END CLASS.
